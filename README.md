# Restaurant Kitchen Management System

This is a Django-based web application for managing a restaurant kitchen. It includes features for managing cooks, dishes, and dish types.

## Architectures
![image](https://github.com/user-attachments/assets/3f887406-4a04-44a7-97df-2a1a43738cf8)


## Features

- **Cooks Management**: Add, update, delete, and view details of cooks.
- **Dishes Management**: Add, update, delete, and view details of dishes.
- **Dish Types Management**: Add, update, delete, and view details of dish types.
- **User Authentication**: Login and logout functionality.
- **Pagination**: Paginated views for lists of cooks, dishes, and dish types.

## Project Structure
restaurant_kitchen/ 

├── core/ 

├── home/ 

├── kitchen/ 

├── static/ 

├── templates/ 

├── manage.py 

└── requirements.txt


## Installation

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd restaurant_kitchen
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Load initial data**:
    ```sh
    python manage.py loaddata kitchen_db_data.json
    ```
    
6. **Create SuperUser**:
    ```sh
    python manage.py createsuperuser
    ```
    - Username: admin.user
    - Email: admin@user.com
    - Password: 1qazcde3
    
7. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Use the admin interface at `http://127.0.0.1:8000/admin/` to manage users and other data.


## Demo
![image](https://github.com/user-attachments/assets/87ab60c5-0256-4922-8864-eaf19dc54d90)
![image](https://github.com/user-attachments/assets/825f2cd9-67ff-4087-be4c-a10ed49a8a6b)
![image](https://github.com/user-attachments/assets/6b35f5d7-3b99-48ca-b351-ee95fa585533)
![image](https://github.com/user-attachments/assets/7994bb0c-5f55-4bac-a5dd-7a092623ac9f)
![image](https://github.com/user-attachments/assets/f7318073-da41-4f20-a987-08e9809ca832)
![image](https://github.com/user-attachments/assets/f64d1b6d-bc94-4a2e-995e-fff6431e00d1)




## Deployment

To deploy the application, you can use Docker. The repository includes a `Dockerfile` and `docker-compose.yml` for containerized deployment.

1. **Build and run the containers**:
    ```sh
    docker-compose up --build
    ```

2. **Access the application**:
    - Application: `http://localhost:5085`
    - Admin: `http://localhost:5085/admin`

## License

This project is licensed under the MIT License. See the [LICENSE.md](django-soft-ui-dashboard/LICENSE.md) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Soft UI Dashboard](https://app-generator.dev/product/soft-ui-dashboard/django/)
