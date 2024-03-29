import argparse
import os

script_dir = os.path.dirname(__file__)


def generate_file(routes_name, template_file, destination_folder, _type):
    template_route_path = os.path.join(script_dir, "templates", template_file)

    if os.path.exists(template_route_path):
        with open(template_route_path, "r") as f:
            template_content = f.read()

        routes_content = template_content.replace("{routes_name}", routes_name)
        destination_file = f'{routes_name}_test' if _type == 'test' else f'{routes_name}'
        destination_path = os.path.join(script_dir, destination_folder, f"{destination_file}.py")

        with open(destination_path, "w") as f:
            f.write(routes_content)
        print(f"Generated {routes_name}.py")
    else:
        print(f"Error: {template_route_path} does not exist")


def generate_files(routes_name):
    generate_file(routes_name, "routes.py", "../farms_api/routes", 'route')
    generate_file(routes_name, "test_routes.py", "../farms_api/tests/routes", 'test')


def main():
    parser = argparse.ArgumentParser(description="Generate files for a project")
    parser.add_argument("routes_name", help="Name of the routes to generate")
    args = parser.parse_args()

    generate_files(args.routes_name)


if __name__ == "__main__":
    main()
