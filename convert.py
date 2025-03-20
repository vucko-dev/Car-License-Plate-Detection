import xml.etree.ElementTree as ET
import os

def convert_to_yolo(xml_folder, output_folder, class_name="licence"):
    os.makedirs(output_folder, exist_ok=True)
    
    for xml_file in os.listdir(xml_folder):
        if not xml_file.endswith(".xml"):
            continue

        tree = ET.parse(os.path.join(xml_folder, xml_file))
        root = tree.getroot()

        width = int(root.find("size/width").text)
        height = int(root.find("size/height").text)

        for obj in root.findall("object"):
            name = obj.find("name").text
            if name != class_name:
                continue

            bndbox = obj.find("bndbox")
            xmin = int(bndbox.find("xmin").text)
            ymin = int(bndbox.find("ymin").text)
            xmax = int(bndbox.find("xmax").text)
            ymax = int(bndbox.find("ymax").text)

            x_center = (xmin + xmax) / (2 * width)
            y_center = (ymin + ymax) / (2 * height)
            bbox_width = (xmax - xmin) / width
            bbox_height = (ymax - ymin) / height

            yolo_annotation = f"0 {x_center} {y_center} {bbox_width} {bbox_height}\n"

            txt_filename = os.path.join(output_folder, xml_file.replace(".xml", ".txt"))
            with open(txt_filename, "w") as f:
                f.write(yolo_annotation)

    print(f"Converted {len(os.listdir(xml_folder))} XML files to YOLO format.")

# Convert annotations for train, valid, test
convert_to_yolo("dataset/train/annotations", "dataset/train/labels")
convert_to_yolo("dataset/valid/annotations", "dataset/valid/labels")
convert_to_yolo("dataset/test/annotations", "dataset/test/labels")
