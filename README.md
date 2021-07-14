Detectron2 is Facebook AI Research's next generation library
that provides state-of-the-art detection and segmentation algorithms.
It is the successor of
[Detectron](https://github.com/facebookresearch/Detectron/)
and [maskrcnn-benchmark](https://github.com/facebookresearch/maskrcnn-benchmark/).
It supports a number of computer vision research projects and production applications in Facebook.

## Installation

See [installation instructions](https://detectron2.readthedocs.io/tutorials/install.html).

## Getting Started

See [Getting Started with Detectron2](https://detectron2.readthedocs.io/tutorials/getting_started.html),
and the [Colab Notebook](https://colab.research.google.com/drive/16jcaJoc6bCFAQ96jDe2HwtXj7BMD_-m5)
to learn about basic usage.

Learn more at our [documentation](https://detectron2.readthedocs.org).
And see [projects/](projects/) for some projects that are built on top of detectron2.

## Model Zoo and Baselines

We provide a large set of baseline results and trained models available for download in the [Detectron2 Model Zoo](MODEL_ZOO.md).

## Training on Cones Dataset

1. If the dataset is not in COCO format conver it to COCO format using the link (https://detectron2.readthedocs.io/en/latest/tutorials/datasets.html)

2. Register the dataset in tools/train_net.py file by adding these lines at the top:
```
from detectron2.data.datasets import register_coco_instances
register_coco_instances("cones_train", {}, "path to train json.json", "path to train images directory")
register_coco_instances("cones_val", {}, "path to val json.json", "path to val images directory")

```
3. Update the dataset names in config file i.e., configs/Base-RCNN-FPN.yaml
```
DATASETS:
  TRAIN: ("cones_train",)
  TEST: ("cones_val",)
```
3. Start the training
```
cd tools/
python train_net.py --num-gpus 4 --config-file ../configs/COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml
```
4. Evaluation
```
python train_net.py --config-file ../configs/COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml --eval-only MODEL.WEIGHTS output/model_0114999.pth
```



## License

Detectron2 is released under the [Apache 2.0 license](LICENSE).

## Citing Detectron2

If you use Detectron2 in your research or wish to refer to the baseline results published in the [Model Zoo](MODEL_ZOO.md), please use the following BibTeX entry.

```BibTeX
@misc{wu2019detectron2,
  author =       {Yuxin Wu and Alexander Kirillov and Francisco Massa and
                  Wan-Yen Lo and Ross Girshick},
  title =        {Detectron2},
  howpublished = {\url{https://github.com/facebookresearch/detectron2}},
  year =         {2019}
}
```
