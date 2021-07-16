from models.town import Town


class MockTownLogic:
    test_town = Town(id=1,
                     created_at="somewhere",
                     name="test",
                     longitude=0,
                     altitude=0,
                     weather_now='fine',
                     forecast='fine')

    @staticmethod
    def get_all(*args, **kwargs):
        return [MockTownLogic.test_town.json()]

    @staticmethod
    def create(*args, **kwargs):
        return MockTownLogic.test_town.json()

    @staticmethod
    def get(town_id, *args, **kwargs):
        if town_id == 1:
            return MockTownLogic.test_town
        else:
            return None

    @staticmethod
    def update(town_id, *args, **kwargs):
        if town_id == 1:
            return MockTownLogic.test_town
        else:
            return None

    @staticmethod
    def delete(*args, **kwargs):
        pass
