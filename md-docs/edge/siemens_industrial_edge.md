# Siemens Industrial Edge 

[Siemens Industrial Edge](https://www.siemens.com/industrial-edge) is an edge computing platform aimed at improving factory operations by bringing data processing and software management directly to the shop floor. It integrates hardware, software and connectivity solutions from both Siemens and its partners, enabling scalable and secure industrial workflows.

The [AI Inference Server](https://www.dex.siemens.com/edge/build-your-solution/ai-inference-server-dk?cclcl=en_EN) is one of the core applications in the Industrial Edge ecosystem. It hosts and runs AI models locally on the edge device, producing predictions from raw input data like images. By running inference on the edge, it avoids the latency and bandwidth costs of sending data to the cloud.

ML cube Platform works in tandem with Siemens AI Inference Server and other applications in the Industrial Edge ecosystem. It receives data from the same acquisition channels that AI Inference Server uses, it receives predictions from it and provides outputs on the desired destination.

## Technical Integration Details

### Cloud Control Plane

ML cube Platform Control Plane is on the private cloud of ML cube and is used to validate the Product Key of the Edge installation. Hence, during the installation an internet connection is required to correctly validate the Product Key to enable the Edge product.
Note: a special testing Product Key is provided for testing the product. 

### Edge Version

ML cube Platform is containerized and compatible with Kubernetes and Docker Compose.
We developed a version specific to Siemens Industrial Edge that uses Docker Compose and provides monitoring functionality directly on Edge.
This version has been created with Industrial Edge Publisher and its creation and deployment are already fully automatized through CI/CD Pipelines that uses iectl.

#### Usage

The base flow of ML cube Platform can be divided into three steps:

1. Data acquisition
2. Data processing
3. Output messaging

As shown in [Figure 1](#fig-architecture), the ML cube Platform is integrated with both MQTT and ZMQ, simplifying communication with other IE applications.
ML cube Platform expects Input data (i.e. images) and Model Prediction data (i.e. bounding boxes). Input data can be provided both through MQTT and ZMQ, while Model Prediction data is expected from MQTT.
The application works in conjunction with Siemens AI Inference Server, which hosts the AI Model and produces predictions. Flow Creator can be leveraged to create a flow that propagates those data to specific ZMQ / MQTT Topics for the ML cube Platform.
After data are acquired from input channels, they are processed internally by ML cube Platform with retention limited to a few days avoiding storage saturation.

ML cube Platform outputs, such as monitoring alerts, are published to other MQTT Topics so that they can be received and processed by other applications.

<figure id="fig-architecture">
  <img src="../../imgs/edge/edge_architectural_scheme.png" alt="Architectural Scheme"/>
  <figcaption>Figure 1: Architectural Scheme</figcaption>
</figure>

#### Data Payloads

ML cube Platform follows payload formats guidelines of Siemens Industrial Edge. After the application is up it sends two MQTT message:

- Metadata for Notifications:

<figure id="metadata-for-notifications">
  <img src="../../imgs/edge/metadata_for_notifications.png"/>
</figure>

- Channel status:

<figure id="channel-status">
  <img src="../../imgs/edge/channel_status.png"/>
</figure>

When data drift occurs then a notification message is sent to the notification channel:

<figure id="channel-status">
  <img src="../../imgs/edge/notification_channel.png"/>
</figure>

The content of `val` field is an object that contains the drift information.
Input payloads of MQTT need to be properly configured before sending them to ML cube Platform. Flow Creator can be used to manipulate raw data before sending them to MQTT. Here the expected payloads:

| Message | Fields |
|---|---|
| MQTT Input Message | **Fields:** <br>- sample_id: str <br>- timestamp: float <br>- arrival_timestamp: float \| null <br>- image_base64: str |
| ZMQ Metadata | **Fields:** <br>- version: str <br>- timestamp: float <br>- detail: Detail[] <br>- linepadding: int <br><br>**Detail fields:** <br>- id: str <br>- seq: int <br>- height: int <br>- width: int <br>- format_ns: str = 'Genicam' <br>- format: str <br>- image: bytes |
| MQTT Prediction Message | **Fields:** <br>- sample_id: str <br>- timestamp: float <br>- arrival_timestamp: float <br>- embedding_vector: float[][] \| null <br>- prediction: PredictionDict <br>- prediction_prob: float[] \| null <br><br>**PredictionDict (Binary Classification):** <br>- prediction: str <br><br>**PredictionDict (Object Detection):** <br>- prediction: BoundingBox[] <br>- prediction_label: str[] <br><br>> BoundingBox is a vector of four floats |
| MQTT Reset Message | **Fields:** <br>- new_model_version: str |

#### Configuration

A JSON configuration file containing all the information about data connectors and monitored tasks is required to install and use the ML cube Platform.
The ML cube Platform uses this configuration file to create all the internal entities and set up the application to acquire data and start monitoring.

You can see an example [Here](https://github.com/ml-cube/ml3-platform-docs/blob/main/edge-config/example_config.json).

#### License and Product Key

The ML cube Platform works with Siemens licence system, so the application is ready to use after the installation is completed.

#### Requirements

The ML cube Platform requires at least 6.5 GB of RAM to run on Edge Device, while the application weighs 3.2 GB. We are working on reducing these quantities, which will lead to a lighter application.