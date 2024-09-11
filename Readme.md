# 🌐 FastAPI Language Prediction API

Welcome to the **FastAPI Language Prediction API**! This project is a machine-learning-powered web service that predicts the language of a given sentence using an SVM classifier. It uses **FastAPI** for serving the model and **TfidfVectorizer** for text transformation.

## 🚀 Features

- **Language Prediction**: Detects the language of an input sentence.
- **Clean Text Functionality**: Automatically removes noise like HTML tags, URLs, stopwords, and accents.
- **Machine Learning**: Uses **Support Vector Machine (SVM)** to classify text.
- **Swagger UI**: Comprehensive API documentation using Swagger.
- **Modular Code Structure**: Well-organized codebase for easy maintainability and scalability.
- **Docker Support**: Seamlessly deploy the application using Docker.

---

## 🏗 Project Structure

```
├── app/
│   ├── api/
│   │   ├── __init__.py    # Package initialization
│   │   └── v1/
│   │       ├── __init__.py    # API versioning
│   │       └── endpoints.py   # API routes and endpoints
│   ├── core/
│   │   ├── __init__.py    # Core initialization
│   │   └── config.py      # Application configuration settings
│   ├── models/
│   │   └── __init__.py    # Machine learning models (SVM, Tfidf, etc.)
│   ├── services/
│   │   ├── __init__.py    # Services initialization
│   │   └── prediction.py  # Business logic for language prediction
│   └── main.py            # FastAPI initialization and application bootstrap
├── dataset/
│   └── dataset.csv        # Training dataset (ignored in git)
├── Dockerfile             # Dockerfile for containerization
├── docker-compose.yml     # Docker Compose configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation (you're reading this!)
```

---

## 🛠 Setup Instructions

Follow these steps to run the application locally or deploy it using Docker.

### 1. **Clone the Repository**

```bash
git clone https://github.com/Damieee/language-prediction-api
cd language-prediction-api
```

### 2. **Setup Environment**

Create a `.env` file in the root directory and add the following values:

```
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=your-region
```

### 3. **Install Dependencies**

Make sure you have Python 3.8+ and install the required packages:

```bash
pip install -r requirements.txt
```

### 4. **Run the Application Locally**

To run the FastAPI app locally, execute:

```bash
uvicorn app.main:app --reload
```

The API documentation will be available at http://localhost:8000/docs.

### 5. **Run with Docker**

To deploy the application using Docker, run the following commands:

```bash
docker-compose up --build
```

This will build the Docker image and run the container. You can access the API at http://localhost:8000.

## 📊 Model Overview

- **Text Cleaning**: Removes HTML, URLs, accents, punctuation, and stopwords.
- **TF-IDF Vectorization**: Converts text to numerical data.
- **SVM Classifier**: Classifies the input text into one of the supported languages.
- **Label Encoding**: Encodes languages for the model.

## 🔥 API Endpoints

### POST `/predict_language/`

**Request:**

```json
{
  "sentence": "Enter the sentence here"
}
```

**Response:**

```json
{
  "sentence": "Enter the sentence here",
  "predicted_language": "English"
}
```

## 📦 Deployment

This project is configured to run in production using Docker. In production, you should ensure the following:

- **Environment Variables**: Ensure that the `.env` file or Docker environment contains production-specific keys and configurations.
- **Docker Compose**: The Docker Compose configuration allows you to spin up the application easily in production environments.

## 🤝 Contributing

Feel free to open issues or submit pull requests for any feature improvements or bug fixes.

1. Fork the repository
2. Create a new feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## 📚 Documentation & Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

## 🔗 Project Links

[![GitHub](https://img.shields.io/badge/GitHub-FastAPI%20Language%20Prediction-blue?style=flat-square&logo=github)](https://github.com/your-username/fastapi-language-prediction)

## 📧 Contact

- **Maintainer**: Dare Ezekiel
- **Email**: joshezekiel.dev@gmail.com
