
class LinkFinder:
    def __init__(self, link_repository) -> None:
        self.__links_repository = link_repository
        
    def find(self, tripId):
        try:
            links = self.__links_repository.find_links_from_trip(tripId)
            
            formatted_link = []
            for link in links:
                formatted_link.append({
                    "id": link[0],
                    "url": link[2],
                    "title": link[3]
                })
            return {
                "body": { "links": formatted_link },
                "status_code": 200
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400
            }