# Last.fm Top Track Viewer

This project displays your most played track on Last.fm for the current month. It consists of a Flask backend API and a React frontend.

## Setup

1. Clone this repository
2. Install Docker and Docker Compose
3. Set your Last.fm API key and username in the `docker-compose.yml` file
4. Run `docker-compose up --build` in the root directory
5. Access the application at `http://localhost:3000`

## Development

- Backend code is located in the `backend` directory
- Frontend code is located in the `frontend` directory

For local development:
1. Start the backend: `cd backend && flask run`
2. Start the frontend: `cd frontend && npm start`

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)