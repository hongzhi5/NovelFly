# NovelFly

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/hongzhi5/NovelFly.git
   cd novelfly

2. **Create a .env file in the root directory with the following content**:

    POSTGRES_USER=your_postgres_username\
    POSTGRES_PASSWORD=your_postgres_user_password\
    DATABASE_HOST=db

3. **Build and Run the Docker Containers**:
    ```bash
    docker-compose up --build

4. **Open your web browser and go to http://localhost:8000.**