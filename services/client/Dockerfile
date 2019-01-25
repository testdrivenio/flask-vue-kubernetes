FROM node:11.7.0-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN ROOT_API=http://localhost:5001 npm run build

EXPOSE 8080

CMD [ "http-server", "dist" ]
