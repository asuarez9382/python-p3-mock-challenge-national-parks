class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, '_name'):
            self._name = name
        
    def trips(self):
        return [ trip for trip in Trip.all if trip.national_park == self ]
    
    def visitors(self):
        visitors_list = []
        for trip in Trip.all:
            if trip.national_park == self and trip.visitor not in visitors_list:
                visitors_list.append(trip.visitor)
        return visitors_list
    
    def total_visits(self):
        visits = 0
        for trip in Trip.all:
            if trip.national_park == self:
                visits += 1
        return visits
    
    def best_visitor(self):
        from collections import Counter
        visitors_list = []
        for trip in Trip.all:
            if trip.national_park == self:
                visitors_list.append(trip.visitor)
        counts = Counter(visitors_list)
        return counts.most_common(1)[0][0]
            


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        import re
        pattern = r"^(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}(st|nd|rd|th)$"
        if isinstance(start_date, str) and len(start_date) >= 7 and re.match(pattern, start_date):
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        import re
        pattern = r"^(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}(st|nd|rd|th)$"
        if isinstance(end_date, str) and len(end_date) >= 7 and re.match(pattern, end_date):
            self._end_date = end_date

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park




class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1<=len(name)<=15:
            self._name = name
        
    def trips(self):
        trips_list = []
        for trip in Trip.all:
            if trip.visitor == self and isinstance(trip, Trip):
                trips_list.append(trip)
        return trips_list
    
    def national_parks(self):
        national_parks_list = []
        for trip in Trip.all:
            if trip.visitor == self and trip.national_park not in national_parks_list:
                national_parks_list.append(trip.national_park)
        return national_parks_list
    
    def total_visits_at_park(self, park):
        total_visits = 0
        for trip in Trip.all:
            if trip.national_park == park and trip.visitor == self:
                total_visits += 1
        return total_visits
