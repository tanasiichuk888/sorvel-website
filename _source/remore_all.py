import sys; sys.argv=["x"]
exec(open("SOURCE_DIR/chapters.py").read().split("if __name__")[0])
for slug in ORDER:
    p = W + slug + ".html"; s = open(p).read()
    a = s.index("    <!-- ============ MORE WORK ============ -->")
    b = s.index("    <!-- ============ NEXT ============ -->")
    s = s[:a] + more_list(slug) + s[b:]
    open(p, "w").write(s); print("more", slug)
