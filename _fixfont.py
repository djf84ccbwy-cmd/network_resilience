# -*- coding: utf-8 -*-
import io
p = r"E:\网络韧性网页制作\网络韧性课题组.html"
s = io.open(p, encoding="utf-8").read()
s = s.replace("padding:11px 13px;font-size:15px;margin-bottom:12px",
              "padding:11px 13px;font-size:16px;margin-bottom:12px")
s = s.replace("border-radius:8px;padding:9px 11px;font-size:14px;font-family:inherit;color:var(--ink);background:#fff",
              "border-radius:8px;padding:9px 11px;font-size:16px;font-family:inherit;color:var(--ink);background:#fff")
io.open(p,"w",encoding="utf-8").write(s)
print("ok")
