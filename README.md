# Object Detection & Tracking using YOLOv8

A computer vision project collection demonstrating real-time object detection, multi-object tracking, and safety compliance monitoring using YOLOv8. The repository contains four progressively advanced applications ranging from basic object detection to traffic analytics and PPE violation detection.

---

## Overview

This project explores practical applications of modern object detection systems using YOLOv8 integrated with tracking and counting algorithms for real-time video analysis.

Implemented functionalities include:
- Real-time object detection
- Vehicle counting and tracking
- Direction-based people counting
- PPE compliance monitoring
- Multi-object tracking using SORT

---

## Projects

### 1. YOLO Basics
**Path:** `chapter-5 running yolo/yolobasics.py`

Runs YOLOv8 inference on a single image and visualizes detected objects with bounding boxes and confidence scores.

### Features
- Image-based object detection
- Bounding box visualization
- Confidence score display

---

### 2. Vehicle Counter
**Path:** `project 1- car counter/car-counter.py`

Detects and tracks vehicles in traffic footage and counts them as they cross a predefined virtual line.

### Features
- Vehicle detection (cars, trucks, buses, motorbikes)
- Multi-object tracking using SORT
- Real-time traffic counting
- Kalman filter–based object association

---

### 3. People Counter
**Path:** `project 2- people counter/people_counter.py`

Tracks people moving on escalators and counts directional movement (up/down) using virtual boundary lines.

### Features
- Human detection and tracking
- Direction-aware counting
- Escalator traffic analytics
- SORT-based tracking pipeline

---

### 4. PPE Detection System
**Path:** `project 3-PPE Detection/PPEDetection.py`

Uses a custom-trained YOLO model (`ppe.pt`) to detect personal protective equipment and identify workplace safety violations.

### Detects
- Hardhats
- Safety Vests
- Gloves
- Face Masks

### Violation Detection
- NO-Hardhat
- NO-Mask
- NO-Safety Vest

---

## Tech Stack

- **YOLOv8 (Ultralytics)** — Real-time object detection
- **SORT** — Multi-object tracking using Kalman Filters
- **OpenCV** — Video processing and frame handling
- **cvzone** — Visualization overlays and UI utilities
- **PyTorch** — Deep learning backend
- **NumPy / SciPy** — Numerical computation

---

## Project Structure

```bash
Object-Detection-YOLO/
├── chapter-5 running yolo/
│   └── yolobasics.py
├── project 1- car counter/
│   └── car-counter.py
├── project 2- people counter/
│   └── people_counter.py
├── project 3-PPE Detection/
│   ├── PPEDetection.py
│   └── ppe.pt
├── videos/
├── requirements.txt
└── README.md
```

---

## Demo Video

Watch the project in action:

👉 https://drive.google.com/file/d/1p4BF101JL3GWsSAzQwJIQvJXracx5niw/view?usp=sharing


