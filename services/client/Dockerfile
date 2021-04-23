FROM node:15-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN ROOT_API=http://localhost:5001 npm run build

EXPOSE 8080

CMD [ "http-server", "dist" ]
