# POC: Setting up Sourcegraph for Local Code Search

This document provides the instructions for running a local instance of Sourcegraph via Docker to provide a human-centric code search experience for the ISA_D repository.

## Prerequisites

*   Docker installed and running on your local machine.
*   The ISA_D repository cloned to your local machine (e.g., at `~/isa_d_project`).

## Step 1: Run the Sourcegraph Docker Container

Execute the following command in your terminal. This will download the Sourcegraph image and start a container.

```bash
docker run -d --publish 7080:7080 --publish 127.0.0.1:3370:3370 --rm \
-v ~/.sourcegraph/config:/etc/sourcegraph \
-v ~/.sourcegraph/data:/var/opt/sourcegraph \
sourcegraph/server:5.3.0
```

**Note:** This command mounts volumes for configuration and data in your home directory (`~/.sourcegraph`) to persist them across container restarts.

## Step 2: Access Sourcegraph and Create an Admin Account

1.  Open your web browser and navigate to `http://localhost:7080`.
2.  You will be prompted to create an admin account. Enter your desired username and password.

## Step 3: Connect to the Local Repository

To make your local code searchable, Sourcegraph needs to be able to access it.

1.  **Get the absolute path** to your local repository clone. For example: `/home/user/isa_d_project`.
2.  **Add the repository to Sourcegraph:**
    *   In the Sourcegraph UI, go to **Settings > Repositories > Add repositories**.
    *   Select **"Connect local code on your machine"**.
    *   Sourcegraph will provide you with a command to run. It will look something like this:

    ```bash
    docker run --rm -it -v "/home/user/isa_d_project:/code" -e "SRC_ENDPOINT=http://host.docker.internal:3370" sourcegraph/src-cli:latest repo add --file <(echo '[{"name": "github.com/isa-superapp/isa-superapp-local", "path": "/code", "enabled": true}]')
    ```
    *   **Important:** You may need to adjust the `SRC_ENDPOINT` depending on your Docker setup. `http://host.docker.internal:3370` often works for Docker Desktop. If not, you may need to use your machine's local IP address.

## Step 4: Start Searching

Once the repository is added, Sourcegraph will begin indexing it. After a few minutes, you should be able to search your entire local ISA_D codebase from the Sourcegraph UI.

This setup provides a powerful, human-centric tool for code discovery and navigation, serving as one half of our comparative POC for code search solutions.
