# CarouselBot

A python script that retrieves Carousel answers by getting answers through an endpoint (no server checking for some reason). **Requires knowledge of user's fullname.**

## Features

- **Login**: Authenticate users with their fullname.
- **Extract Answers**: Retrieve answers for assigned work.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/plop-dev/CarouselBot.git
    ```

2. Navigate to the project directory:

    ```sh
    cd CarouselBot
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Add a config file (.env):

    ```env
    FORENAME = "Plop"
    SURNAME = "Plop"
    LINK = "<https://app.carousel-learning.com/quiz/736120e0-5659-4bfc-a2b0-f604c9123e87c>"
    INFO = "bold blue"
    SUCCESS = "bold green"
    ```

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please contact <him@maximec.dev>.

---

<small>this readme is mostly ai so don't judge my ai english.</small>
