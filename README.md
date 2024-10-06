# 📋 Healthcare Task Management System

Welcome to the **Healthcare Task Management System**! This application streamlines the management of healthcare tasks between **managers** (gestores) and **collaborators** (colaboradores). It allows managers to organize, assign, and monitor tasks related to **patients**, while collaborators can view and complete the tasks assigned to them.

## 🌟 Features

### 👥 User Roles:
- **Gestor (Manager)**:
  - Add and manage patients and collaborators.
  - Assign tasks to collaborators for specific patients.
  - Monitor task progress and update patient information.
- **Colaborador (Collaborator)**:
  - View the list of patients and tasks assigned by the manager.
  - Mark tasks as completed once finished.

### 🏥 Patient Management:
- Add new patients with essential details (name, age, contact information, address, etc.).
- Update patient information easily, including their current address.
- View and manage patient-specific tasks.

### 📋 Task Management:
- Assign tasks related to a specific patient to a collaborator.
- Collaborators can mark tasks as completed after execution.
- View all ongoing and completed tasks for each patient.

### 📍 Address Management:
- Manage patient addresses, ensuring the most up-to-date contact information.
- View historical addresses for each patient.

## 🛠️ Technologies Used

- **Backend**: Django (Python)
- **Database**: SQLite (should replace)
- **Deployment**: Docker (TODO)

## 🚀 Getting Started

### Prerequisites:
- Python 3.8+
- Django 4.0+
- SQLite

### Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/guimaraesr-y/healthcare-task-management.git
   cd healthcare-task-management
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the Django server:
   ```bash
   python manage.py runserver
   ```

6. Access the app at:
   ```bash
   http://127.0.0.1:8000/
   ```

## 🧩 API Endpoints (For Future Implementation)

- `GET /api/patients/`: Fetch all patients.
- `GET /api/patients/<id>/`: Fetch a specific patient.
- `POST /api/patients/`: Add a new patient.

- `GET /api/collaborators/`: Fetch all collaborators.
- `GET /api/collaborators/<id>/`: Fetch a specific collaborator.
- `POST /api/collaborators/`: Add a new collaborator.

- `GET /api/tasks/`: View all tasks.
- `GET /api/tasks/<id>/`: View a specific task.
- `POST /api/tasks/`: Assign a new task to a patient.
- `PUT /api/tasks/<id>/`: Mark a task as completed.

## 🎨 Future Enhancements

- Add a **Frontend** using React for a more user-friendly interface.
- Implement notifications to alert collaborators about new tasks or updates.
- **Mobile-Friendly**: Optimize the interface for mobile healthcare workers.
- **Analytics Dashboard**: Provide managers with insights into task completion rates and patient care.

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with any improvements or bug fixes.

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by [Ryan Guimarães](https://github.com/guimaraesr-y)
