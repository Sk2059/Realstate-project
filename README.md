# Real Estate Crafters International Pvt Ltd

A comprehensive real estate platform built with React frontend and Django backend, offering property buying, selling, rental services, and repair/maintenance solutions.

## 🏢 About

Real Estate Crafters International Pvt Ltd is a full-service real estate company providing:
- Property buying and selling services
- Rental property management
- Property repair and maintenance
- Professional consultation

## 🚀 Tech Stack

### Frontend
- **React 18** with TypeScript
- **Vite** for build tooling
- **Tailwind CSS** for styling
- **shadcn/ui** component library
- **React Router** for navigation
- **React Query** for data fetching
- **React Hook Form** with Zod validation

### Backend
- **Django 5.0.2** with Django REST Framework
- **PostgreSQL** database
- **Django Migrations** for database management

## 📁 Project Structure

```
proj/
├── front/                 # React frontend application
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Page components
│   │   ├── contexts/      # React contexts (Language, etc.)
│   │   ├── back/          # API integration layer
│   │   └── hooks/         # Custom React hooks
│   ├── public/            # Static assets
│   └── package.json
├── back/                  # Django backend application
│   ├── properties/        # Property management app
│   ├── projects/          # Project management app
│   ├── contactss/         # Contact and service requests app
│   └── migrations/        # Database migrations
└── .vscode/               # VS Code configuration
```

## 🛠️ Installation & Setup

### Prerequisites
- Node.js (v16 or higher)
- Python 3.8+
- PostgreSQL

### Frontend Setup

```bash
# Navigate to frontend directory
cd proj/front

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

### Backend Setup

```bash
# Navigate to backend directory
cd proj/back

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## 🌟 Features

### 🏠 Property Management
- Browse available properties
- Advanced search and filtering
- Property details with image galleries
- Contact property owners directly

### 📞 Contact & Communication
- Contact form for inquiries
- Service request system
- Multi-language support (English/Nepali)
- Admin dashboard for managing communications

### 🔧 Repair Services
- Request repair and maintenance services
- Service type categorization
- Urgency level selection
- File upload for service requests

### 👨‍💼 Admin Panel
- Manage properties and projects
- View and respond to contact messages
- Handle service requests
- User authentication and authorization

### 🌐 Multi-language Support
- English and Nepali language options
- Context-based language switching
- Localized content and UI

## 📱 Pages

- **Home** - Landing page with featured properties
- **Buy** - Property listings with search/filter
- **Sell** - Property selling form
- **About** - Company information and client reviews
- **Contact** - Contact form and company details
- **Repairing** - Repair service request form
- **Others** - Additional services
- **Admin** - Administrative dashboard

## 🎨 UI Components

Built with shadcn/ui components including:
- Cards, Buttons, Forms
- Dialogs, Dropdowns, Navigation
- Data tables and pagination
- Toast notifications
- Responsive design

## 📧 Contact Information

- **Phone**: +977 970-7362231
- **Email**: realestatecrafters1@gmail.com
- **Website**: [Lovable Project](https://lovable.dev/projects/78a356d3-a2de-417a-bc1c-d8cdf478fca4)

## 🚀 Deployment

### Frontend Deployment
The frontend can be deployed using:
- Lovable platform (recommended)
- Vercel, Netlify, or similar platforms
- Custom domain support available

### Backend Deployment
- Configure production database
- Set up environment variables
- Deploy to cloud platforms (AWS, Heroku, etc.)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is proprietary software owned by Real Estate Crafters International Pvt Ltd.

## 🆘 Support

For technical support or business inquiries, please contact us through our website or email.
