![Python 3.7, 3.8, 3.9](https://img.shields.io/badge/Python-3.7%2C%203.8%2C%203.9-3776ab.svg?maxAge=2592000)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

### Video-Ditor
  A simple video editor python package
  Affiliated to [Bank of Ghana Fx Rates](https://pypi.org/project/bank-of-ghana-fx-rates/),
  [GhanaNews-Scraper](https://pypi.org/project/ghananews-scraper/), and
  [GhanaShops-Scraper](https://pypi.org/project/ghanashops-scraper/)

### How to install
```shell
pip install video-ditor
```
### Install using:
```shell
# OR
git clone https://github.com/donwany/Video-Ditor.git
cd Video-Ditor
make pre-release
```

### Download YouTube/Facebook/Twitter Videos
```bash
# Using CLI
ytube -u https://www.youtube.com/watch?v=fqi8cvN1hrI

ytube --url https://twitter.com/kwadwosheldon/status/1673856306136981504

ytube --url https://www.facebook.com/gtvghana/videos/1219922122741862
```

### Join Videos
```bash
python main.py \
-c one.mp4 two.mp4 three.mp4 \ 
-o output.mp4

# Using CLI
concat \
-c one.mp4 two.mp4 three.mp4 \ 
-o output.mp4
```

### Cut Videos
```bash
python main.py \
-i input.mp4 \
-o output.mp4 \
-s "00:00:00" \
-e "00:00:00"

# Using CLI
slice \
-i input.mp4 \
-o output.mp4 \
-s "00:00:00" \
-e "00:00:00"
```

### Watermark Videos
```bash
python main.py -i input.mp4 -w james.png -x 500 -o water_output.mp4

# Using CLI
watermark -i input.mp4 -w james.png -x 500 -p "left,bottom" -o water_output.mp4
```
### Add Background and Overlay Video
```bash
python main.py -b background_video.mp4 -o overlay_video.mp4 -x final1.mp4 -p 150 -v 0.10 -bv 1.0

# Using CLI
background -b background_video.mp4 -o overlay_video.mp4 -x final1.mp4 -p 150 -v 0.10 -bv 1.0
```

### Add Text to Video
  + text position: "left,top" , "left,bottom", "right,bottom"
```shell
add_text -i input.mp4 -o output.mp4 -s "@the_data_prof" -f 50 -t "blue" -p "center,top"
```

BuyMeCoffee
-----------
[![Build](https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png)](https://www.buymeacoffee.com/theodondrew)

Credits
-------
-  `Theophilus Siameh`
<div>
    <a href="https://twitter.com/tsiameh"><img src="https://img.shields.io/twitter/follow/tsiameh?color=blue&logo=twitter&style=flat" alt="tsiameh twitter"></a>
</div>