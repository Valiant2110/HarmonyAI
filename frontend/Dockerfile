# Use official Node image
FROM node:20

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build

# Use Vite preview server
RUN npm install -g serve
CMD ["serve", "-s", "dist", "-l", "5173"]
