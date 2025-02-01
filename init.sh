#!/bin/sh


open_url() {
    local url=$1

    case "$(uname -s)" in
        Linux*)
            if grep -qi microsoft /proc/version; then
                # WSL
                cmd.exe /c start "$url" >/dev/null 2>&1
            else
                # Regular Linux
                xdg-open "$url" >/dev/null 2>&1
            fi
            ;;
        Darwin*)
            # macOS
            open "$url" >/dev/null 2>&1
            ;;
        *)
            echo "Unsupported operating system"
            exit 1
            ;;
    esac
}

git init -b master
git add .
git commit -m "Initial commit"
cp .docker.env .env
docker compose build
docker compose up -d db redis
sleep 2
docker compose run --rm web python manage.py generate_tailwind_directories
docker compose run --rm web npm i && npm run tailwind:build
docker compose run --rm web python manage.py migrate
docker compose run --rm web python manage.py makesuperuser

docker compose up -d
sleep 1

count=0; max_retries=5; until curl -s -f -o /dev/null "http://127.0.0.1:9000" || [ $count -ge $max_retries ]; do echo "Waiting... $((count+1))/$max_retries"; count=$((count+1)); sleep 1; done; if [ $count -lt $max_retries ]; then echo "Site is up!"; else echo "App is still down after $max_retries retries"; exit 1; fi

open_url http://127.0.0.1:9000
echo "Open your browser at http://127.0.0.1:9000"