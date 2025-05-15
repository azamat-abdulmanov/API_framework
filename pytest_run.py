import pytest
import subprocess
import argparse
import os
import shutil
import sys
from framework_core.logger_config import setup_logger

logger = setup_logger(__name__, level="DEBUG")  # или INFO, WARNING, ERROR


def get_allure_path():
    env_path = os.environ.get("ALLURE_PATH")
    if env_path and os.path.exists(env_path):
        return env_path

    path_from_which = shutil.which("allure")
    if path_from_which:
        return path_from_which

    fallback_path = r"C:\Users\user1\scoop\apps\allure\current\allure.exe"
    if os.path.exists(fallback_path):
        return fallback_path

    raise FileNotFoundError(
        "Allure executable not found. Set ALLURE_PATH or add Allure to PATH."
    )


def run_tests():
    logger.info("🚀 Запуск тестов с Allure...")
    pytest.main(["--alluredir=allure-results"])


def generate_allure_report():
    allure_path = get_allure_path()
    command = [allure_path, "generate", "allure-results", "-o", "allure-report", "--clean"]

    logger.info(f"🔧 Генерация отчета: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        logger.error("❌ Ошибка генерации отчета:")
        logger.error(result.stderr)
        sys.exit(result.returncode)
    else:
        logger.info("✅ Отчет успешно сгенерирован.")
        logger.debug(result.stdout)


def open_allure_report():
    allure_path = get_allure_path()
    logger.info("📂 Открытие Allure-отчета...")
    subprocess.run([allure_path, "open", "allure-report"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tests and generate Allure report.")
    parser.add_argument("--open", action="store_true", help="Open the Allure report after generation.")
    parser.add_argument("--log_level", default="INFO", help="Logging level (DEBUG, INFO, WARNING, ERROR)")
    args = parser.parse_args()

    logger = setup_logger(__name__, level=args.log_level)

    run_tests()
    generate_allure_report()

    if args.open:
        open_allure_report()