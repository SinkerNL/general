# Tutorial
For the first requirement, we need a simple frontend. In order to do so, I will use a frontend called "lowdefy".

## Installing lowdefy
To use lowdefy, we need to have npm/npx installed. This is installed by first installing npm. This can be done with the following link (in this case I'm using Manjaro Linux):

`sudo pacman -Syu nodejs npm`

Next, Lowdefy should be initialized. This can be done with the following command:
`npx lowdefy@latest init`
This process can take a while. After successful installation, a lowdefy.yaml is created in the folder you run the command. If not, it means that it has failed. 

Now we can run the frontend running: 
`npx lowdefy@latest dev`

## Lowdefy on M1
Please be aware that it does not run 'out-of-the-box' on a M1 Mac. You need to install nvm v16 and make sure you're running terminal in Rosetta (x86-64 instead of amd64). In general, it should then work. 

## Run the docker-compose
In order to run the full-stack, we need to run docker-compose. This can be done with the following command:
`docker-compose up -d --build`