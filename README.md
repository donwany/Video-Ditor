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

### Join Videos
```bash
python main.py \
-c africa1.mp4 gabby.mp4 \ 
-o gabby_africa.mp4

# Using CLI
concat \
-c africa1.mp4 gabby.mp4 \ 
-o gabby_africa.mp4
```

### Cut Videos
```bash
python main.py \
-i africa1.mp4 \
-o gabby_africa.mp4 \
-s "00:00:00" \
-e "00:00:00"

# Using CLI
slice \
-i africa1.mp4 \
-o gabby_africa.mp4 \
-s "00:00:00" \
-e "00:00:00"
```

### Watermark Videos
```bash
python main.py -i gabby.mp4 -w james.png -x 500 -o water_output.mp4

# Using CLI
watermark -i gabby.mp4 -w james.png -x 500 -o water_output.mp4
```
### Add Background and Overlay Video
```bash
python main.py -b gabby.mp4 -o IWILL.mp4 -x final1.mp4 -p 150 -v 0.10 -bv 1.0

# Using CLI
background -b gabby.mp4 -o IWILL.mp4 -x final1.mp4 -p 150 -v 0.10 -bv 1.0
```

### Download YouTube Videos
```bash

# Using CLI
ytube -u https://www.youtube.com/watch?v=fqi8cvN1hrI

ytube -u https://twitter.com/kwadwosheldon/status/1673856306136981504

ytube -u https://www.facebook.com/gtvghana/videos/1219922122741862
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