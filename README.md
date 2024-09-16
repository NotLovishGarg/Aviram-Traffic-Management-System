# Aviram - AI-Based Traffic Management System

![Aviram Logo](./Application/frontend/assets/logo.png)

## Overview
**Aviram** is an AI-powered, real-time traffic management system that leverages advanced machine learning algorithms, OpenCV, and real-time traffic data to optimize traffic flow, prioritize emergency vehicles, and enhance road safety. The system is scalable and designed to evolve with advancements in AI and urban infrastructure, making it a future-proof solution for modern cities.

## Features
- **Real-Time Traffic Analysis**: Uses AI and OpenCV to achieve 84% accuracy in detecting traffic density, helping reduce congestion.
- **Traffic Prediction**: Estimates traffic flow in non-camera zones using historical and nearby data.
- **Emergency Vehicle Prioritization**: Clears paths for emergency vehicles within 5 seconds by adjusting traffic lights.
- **GreenWave Traffic Flow**: Synchronizes traffic lights to create a continuous flow, reducing stop times by up to 15%.
- **Environmental Benefits**: Reduces CO2 emissions by 10% through efficient traffic management.
- **Pedestrian & Animal Safety**: Includes features to prioritize vulnerable road users, enhancing overall road safety.
- **Scalable Architecture**: Adapts to cities of various sizes and traffic patterns, ensuring efficient traffic management.

## System Architecture
- **Traffic Density Detection**: Real-time traffic analysis using OpenCV image processing models.
- **AI-Powered Traffic Signal Control**: Adjusts traffic lights dynamically based on real-time vehicle density data.
- **Bharat Maps Integration**: Utilizes Bharat Maps for traffic predictions in areas without camera coverage.
- **Emergency Vehicle Detection**: Detects emergency vehicles in real-time, prioritizing lane clearance for faster response times.

## Technologies Used
- **Python & OpenCV**: For image processing and real-time traffic density detection.
- **Flutter**: Cross-platform mobile application for users to interact with traffic updates and navigation.
- **Bharat Maps**: For predicting traffic flow in non-camera areas.
- **AI & Machine Learning**: For adaptive traffic signal control and predictive traffic analysis.

## Application (Flutter)
The **Aviram Flutter application** provides users with a comprehensive dashboard that displays real-time traffic updates, emergency alerts, and live navigation. It includes features such as:
- **Navigation Integration**: Displays the user’s current location and supports real-time navigation to any destination.
- **Real-Time Alerts**: Provides live notifications about traffic conditions and emergency vehicle routes.
- **Responsive Design**: Ensures a seamless experience across devices with varying screen sizes.
