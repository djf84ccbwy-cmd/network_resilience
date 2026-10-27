# -*- coding: utf-8 -*-
import io, re, base64, os
p = r"E:\网络韧性网页制作\网络韧性课题组.html"
s = io.open(p, encoding="utf-8").read()
outdir = r"E:\网络韧性网页制作\assets"
os.makedirs(outdir, exist_ok=True)
# 提取所有 base64 图片
imgs = re.findall(r'data:image/(jpeg|png);base64,([A-Za-z0-9+/=]+)', s)
print("found images:", len(imgs))
for i,(ext,b64) in enumerate(imgs):
    data = base64.b64decode(b64)
    # 第一张是 logo，第二张 hero，第三张成员照；按大小判断
    fn = os.path.join(outdir, "img_%d.%s" % (i+1, ext))
    with open(fn,"wb") as f:
        f.write(data)
    print(fn, len(data), "bytes")
