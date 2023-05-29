from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import requests
import difflib


def similarity(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    return matcher.ratio()


urls = [
    "https://img.freepik.com/premium-photo/several-dogs-run-and-playing-together-outdoors-golden-retriever-toller-dog_721668-166.jpg",
    "http://images.cocodataset.org/val2017/000000039769.jpg",
]
my_file = open("result.txt", "w+")
result = ""
for url in urls:
    image = Image.open(requests.get(url, stream=True).raw)

    processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
    model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    # convert outputs (bounding boxes and class logits) to COCO API
    # let's only keep detections with score > 0.9
    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(
        outputs, target_sizes=target_sizes, threshold=0.9
    )[0]

    for score, label, box in zip(
        results["scores"], results["labels"], results["boxes"]
    ):
        box = [round(i, 2) for i in box.tolist()]
        print(f"{model.config.id2label[label.item()]} {round(score.item(), 3)} {box}")
        my_file.write(
            f"{model.config.id2label[label.item()]} {round(score.item(), 3)} {box}\n"
        )
        result += (
            f"{model.config.id2label[label.item()]} {round(score.item(), 3)} {box}\n"
        )
my_file.close()
f = open("my_result.txt", "r")
res1 = f.read()
f.close()
print(f"Result: {similarity(result, res1) * 100}%")
