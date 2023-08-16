from ultralytics import YOLO

# Load a YOLOv8 model
model = YOLO(r"E:\yolov8-cls\runs\classify\train\weights\best.pt")

# Export the model
model.export(format="onnx", opset=12, simplify=True, dynamic=False, imgsz=224)


#命令行参数https://docs.ultralytics.com/modes/export/#arguments

