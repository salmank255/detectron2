# if your dataset is in COCO format, this cell can be replaced by the following three lines:



from detectron2.data.datasets import register_coco_instances
register_coco_instances("cones_train", {}, "/mnt/mars-alpha/salman/work_with_Izzedddin/cones_dectection/detectron2/datasets/cones_dataset/good/images/annotations/instances_train.json", "/mnt/mars-alpha/salman/work_with_Izzedddin/cones_dectection/detectron2/datasets/cones_dataset/good/images/train")
register_coco_instances("cones_val", {}, "/mnt/mars-alpha/salman/work_with_Izzedddin/cones_dectection/detectron2/datasets/cones_dataset/good/images/annotations/instances_val.json", "/mnt/mars-alpha/salman/work_with_Izzedddin/cones_dectection/detectron2/datasets/cones_dataset/good/images/val")
