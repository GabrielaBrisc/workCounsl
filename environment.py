from browser import Browser
from pages.add_draft_service_page import AddDraftService
from pages.add_public_service_page import AddPublicService
from pages.sign_in_page import Sign_in
from pages.onboarding_provider_page import OnboardingProvider
from pages.onboarding_consumer_page import OnboardingConsumer
from pages.search_service_page import SearchService
from pages.navigate_menus_page import Side_menu_navigation


def before_all(context):
    context.browser = Browser() ## obj de tip browser
    context.sign_in_page = Sign_in()
    context.onboarding_consumer_page = OnboardingConsumer()
    context.onboarding_provider_page = OnboardingProvider()
    context.search_service_page = SearchService()
    context.navigate_menus_page = Side_menu_navigation()
    context.add_draft_service_page = AddDraftService()
    context.add_public_service_page = AddPublicService()

#dupa executarea tuturor testelor, vrem sa inchidem browser-ul
def after_all(context):
    context.browser.close()