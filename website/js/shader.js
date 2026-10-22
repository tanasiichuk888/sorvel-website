// Hero background: a slow, domain-warped "ember smoke" field in raw WebGL.
// Brighter on the right (behind the work wall), calm on the left (behind the headline).
// The cursor bends the flow and leaves a soft glow.
(function () {
  const canvas = document.querySelector(".hero__shader");
  if (!canvas) return;
  const gl = canvas.getContext("webgl", { antialias: false, alpha: false, powerPreference: "high-performance" });
  if (!gl) { canvas.style.background = "radial-gradient(80% 70% at 85% 60%, rgba(59,107,255,.22), transparent 70%)"; return; }

  const REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const MOBILE = matchMedia("(max-width: 760px)").matches;

  const vert = `attribute vec2 p; void main(){ gl_Position = vec4(p, 0.0, 1.0); }`;
  const frag = `
    precision highp float;
    uniform vec2 uRes; uniform float uTime; uniform vec2 uMouse; uniform float uMob;
    float hash(vec2 p){ return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
    float noise(vec2 p){
      vec2 i = floor(p), f = fract(p); vec2 u = f*f*(3.0-2.0*f);
      return mix(mix(hash(i), hash(i+vec2(1,0)), u.x), mix(hash(i+vec2(0,1)), hash(i+vec2(1,1)), u.x), u.y);
    }
    float fbm(vec2 p){
      float v = 0.0, a = 0.5; mat2 m = mat2(1.6, 1.2, -1.2, 1.6);
      for (int i = 0; i < 5; i++){ v += a*noise(p); p = m*p; a *= 0.5; }
      return v;
    }
    void main(){
      vec2 uv = gl_FragCoord.xy / uRes;
      vec2 p = (gl_FragCoord.xy - 0.5*uRes) / uRes.y;
      vec2 m = (uMouse - 0.5*uRes) / uRes.y;
      float md = length(p - m);
      p += normalize(p - m + 1e-4) * -0.10 * exp(-md*2.6);   // cursor bends the flow

      float t = uTime * 0.05;
      vec2 q = vec2(fbm(p*1.3 + vec2(0.0, t)), fbm(p*1.3 + vec2(5.2, 1.3) - t));
      vec2 r = vec2(fbm(p*1.5 + 3.6*q + vec2(1.7, 9.2) + t*1.3), fbm(p*1.5 + 3.6*q + vec2(8.3, 2.8) - t));
      float f = fbm(p*1.1 + 3.8*r);

      float ridge = pow(1.0 - abs(f*2.0 - 1.0), 7.0);     // thin glowing filaments
      float body  = smoothstep(0.35, 0.95, f);

      vec3 bg    = vec3(0.039, 0.043, 0.055);
      vec3 ember = vec3(0.231, 0.42, 1.0);
      vec3 peach = vec3(0.66, 0.75, 1.0);
      vec3 deep  = vec3(0.03, 0.07, 0.30);

      // calm on the left, alive on the right; on phones it lives at the bottom
      float side = mix(smoothstep(0.15, 1.05, uv.x*0.95 + (1.0-uv.y)*0.25), smoothstep(0.25, 0.95, 1.0-uv.y), uMob);
      vec3 col = bg;
      col += deep  * body * 0.75 * side;
      col += ember * ridge * 0.52 * side;
      col += peach * pow(ridge, 4.0) * 0.45 * side;
      col += ember * 0.10 * exp(-md*3.2);                  // cursor glow
      col *= 1.0 - 0.45 * pow(length(uv - vec2(0.55, 0.5)), 2.0);
      gl_FragColor = vec4(col, 1.0);
    }`;

  function sh(type, src) {
    const s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) console.warn(gl.getShaderInfoLog(s));
    return s;
  }
  const prog = gl.createProgram();
  gl.attachShader(prog, sh(gl.VERTEX_SHADER, vert));
  gl.attachShader(prog, sh(gl.FRAGMENT_SHADER, frag));
  gl.linkProgram(prog);
  gl.useProgram(prog);
  const buf = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buf);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
  const loc = gl.getAttribLocation(prog, "p");
  gl.enableVertexAttribArray(loc);
  gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
  const uRes = gl.getUniformLocation(prog, "uRes"), uTime = gl.getUniformLocation(prog, "uTime"),
        uMouse = gl.getUniformLocation(prog, "uMouse"), uMob = gl.getUniformLocation(prog, "uMob");

  const scale = MOBILE ? 0.5 : 0.6;                       // render small, upscale; smoke hides it
  let W = 0, H = 0;
  function resize() {
    W = Math.max(1, Math.round(canvas.clientWidth * scale));
    H = Math.max(1, Math.round(canvas.clientHeight * scale));
    canvas.width = W; canvas.height = H;
    gl.viewport(0, 0, W, H);
  }
  addEventListener("resize", resize); resize();

  const mouse = { x: 0.78, y: 0.45 }, target = { x: 0.78, y: 0.45 };
  addEventListener("pointermove", (e) => {
    const r = canvas.getBoundingClientRect();
    target.x = (e.clientX - r.left) / r.width;
    target.y = (e.clientY - r.top) / r.height;
  }, { passive: true });

  let visible = true;
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(canvas);

  const start = performance.now();
  function frame(now) {
    requestAnimationFrame(frame);
    if (!visible || document.hidden) return;
    mouse.x += (target.x - mouse.x) * 0.05;
    mouse.y += (target.y - mouse.y) * 0.05;
    gl.uniform2f(uRes, W, H);
    gl.uniform1f(uTime, REDUCED ? 12.0 : 12.0 + (now - start) / 1000);
    gl.uniform2f(uMouse, mouse.x * W, (1 - mouse.y) * H);
    gl.uniform1f(uMob, MOBILE ? 1 : 0);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
  }
  requestAnimationFrame(frame);
})();
