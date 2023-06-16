# C23-PC734-SehatKu

<p>SehatKu app is an ML-powered food ingredient analysis app that allows users to scan or take
photos of food product packaging to identify the ingredients and their associated health benefits.

The team attempted to build a text detection model using TensorFlow Lite as the final deployment. Although the model achieved an impressive accuracy of 93%, deployment was not pursued within the project scope. Challenges related to incorrect predictions and potential overfitting were encountered. As an alternative approach, the YOLOv5 model was explored for region detection and achieved a mean Average Precision (mAP) of 58%. However, due to time constraints and limited resources, integration with the text detection model was not possible. EasyOCR was implemented as a workaround to successfully read food ingredient labels, but never made it to the deployment stage.


</p>

## Features
<ol>
  <li>
    <h5>OCR with Self-built Model</h5>
    <p></p>
  </li>
  <li>
    <h5>OCR with PyTesseract/EasyOCR Library</h5>
    <p></p>
  </li>
</ol>

## Datasets
<ol>
  <li>
    <h5>Alphanumeric Recognition</h5>
    <p>https://www.kaggle.com/datasets/preatcher/standard-ocr-dataset</p>
  </li>
  <li>
    <h5>Composition Product Images</h5>
    <p>https://drive.google.com/drive/folders/1KCuI2eLSAEcUsf3ksG07VTuY_B7W4X0K?usp=sharing</p>
  </li>
</ol>
