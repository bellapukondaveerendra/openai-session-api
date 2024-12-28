# OpenAI Session Management API

A simple and scalable API for managing chat sessions powered by OpenAI's GPT models. This API enables developers to create, manage, and retrieve chat sessions while storing chat histories in MongoDB.

---

## Features

- **Session Management**: Create unique chat sessions with a `sessionId`.
- **Chat Continuity**: Send messages and receive AI-powered responses while storing the conversation history.
- **History Retrieval**: Fetch the complete chat history for any session.
- **Scalable Storage**: Uses MongoDB to store sessions and chat logs.

---

## Tech Stack

- **FastAPI**: High-performance API framework.
- **MongoDB**: Database for storing sessions and chat histories.
- **OpenAI GPT-3.5**: AI-powered text generation.

---

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

- **Python 3.9+**
- **MongoDB**: Local or Cloud (e.g., MongoDB Atlas)
- **OpenAI API Key**: Sign up at [OpenAI](https://platform.openai.com/signup/)

### Installation

1.  **Clone the repository**:

        git clone https://github.com/bellapukondaveerendra/openai-session-api

    cd openai-session-api

2.  **Create and activate a virtual environment**:

        python -m venv venv

    source venv/bin/activate # On Windows: venv\Scripts\activate

3.  **Install dependencies**:

    `pip install -r requirements.txt`

4.  **Set up environment variables**:

    - Create a `.env` file in the root directory:

      - OPENAI_API_KEY=your-api-key-here
      - MONGO_URI=mongodb://localhost:27017/

    - Replace `your-api-key-here` with your OpenAI API key.
    - Update the `MONGO_URI` if you're using a cloud database like MongoDB Atlas.

5.  **Start the MongoDB server (if running locally)**:

    `mongod`

6.  **Run the application**:

    `uvicorn app.main:app --reload`

7.  **Access the API documentation**:

    - Open http://127.0.0.1:8000/docs for the interactive Swagger UI.

---

## API Endpoints

### 1\. **Create Session**

- **Method**: `POST`
- **Endpoint**: `/session`
- **Description**: Creates a new session and returns a `sessionId`.
- **Response**:

  `{
    "sessionId": "unique-session-id"
}`

---

### 2\. **Send Message**

- **Method**: `POST`
- **Endpoint**: `/chat`
- **Description**: Send a user message and get a response from the AI.
- **Request Body**:

  `{
    "sessionId": "unique-session-id",
    "message": "Your message here"
}`

- **Response**:

  `{
    "response": "AI's response to your message"
}`

---

### 3\. **Get Session History**

- **Method**: `GET`
- **Endpoint**: `/session/{sessionId}/history`
- **Description**: Fetch the complete chat history for a session.
- **Response**:

  `{
    "sessionId": "unique-session-id",
    "history": [
        { "role": "user", "content": "Your message" },
        { "role": "assistant", "content": "AI's response" }
    ]
}`

---

## Future Enhancements

- **Session Expiry**: Add automatic cleanup of old sessions.
- **Summarization**: Implement chat history summarization for long conversations.
- **User Authentication**: Secure sessions with user accounts.
- **Analytics**: Provide insights into API usage and performance.

---

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

---

## Contact

- **Author**: Veerendra Bellapukonda
- **LinkedIn**: https://www.linkedin.com/in/veerendra-bellapukonda-3a1245235/
- **GitHub**: https://github.com/bellapukondaveerendra

---

Happy coding! 🚀
