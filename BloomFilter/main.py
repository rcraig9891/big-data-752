from bloom import Bloom

valid_emails = [
    "john.doe@example.com", "jane.smith@example.com", "michael.johnson@example.com", "sarah.williams@example.com",
    "james.brown@example.com", "emily.davis@example.com", "david.miller@example.com", "lisa.garcia@example.com",
    "robert.wilson@example.com", "mary.rodriguez@example.com", "william.martinez@example.com",
    "emma.hernandez@example.com", "matthew.robinson@example.com", "olivia.moore@example.com",
    "joseph.hall@example.com", "sophia.young@example.com", "jacob.lopez@example.com", "isabella.gonzalez@example.com",
    "ethan.lewis@example.com", "mia.jackson@example.com", "alexander.harris@example.com", "ava.clark@example.com",
    "daniel.lewis@example.com", "madison.lee@example.com", "anthony.walker@example.com", "grace.perez@example.com",
    "noah.hall@example.com", "chloe.green@example.com", "samuel.hill@example.com", "sophie.baker@example.com",
    "logan.nguyen@example.com", "alexandra.king@example.com", "gabriel.carter@example.com", "ella.collins@example.com",
    "benjamin.ross@example.com", "mia.james@example.com", "christopher.gray@example.com", "hannah.evans@example.com",
    "jackson.turner@example.com", "amelia.stewart@example.com", "ethan.morris@example.com",
    "lucas.price@example.com", "natalie.cooper@example.com", "jack.morgan@example.com", "lily.hughes@example.com",
    "aiden.bell@example.com", "zoey.brooks@example.com", "owen.ward@example.com", "brooklyn.murphy@example.com",
    "caleb.wood@example.com", "ellie.rogers@example.com", "wyatt.stone@example.com", "audrey.rivera@example.com",
    "gabriel.watson@example.com", "savannah.kelly@example.com", "isaac.alexander@example.com",
    "lucas.mitchell@example.com", "leah.adams@example.com", "dylan.cook@example.com", "madelyn.bailey@example.com",
    "grayson.sanders@example.com", "brooklyn.phillips@example.com", "jaxon.gutierrez@example.com",
    "skylar.ellis@example.com", "joseph.fernandez@example.com", "lillian.collins@example.com", "leo.barnes@example.com",
    "claire.ross@example.com", "lincoln.hall@example.com", "maya.morris@example.com", "carter.martin@example.com",
    "lucas.russell@example.com", "aubrey.dixon@example.com", "julian.gomez@example.com", "sara.alexander@example.com",
    "josiah.wood@example.com", "nora.griffin@example.com", "christian.lee@example.com", "elizabeth.mendoza@example.com",
    "luke.harrison@example.com", "gabriella.hudson@example.com", "jonathan.cruz@example.com", "anna.baker@example.com",
    "isaiah.nguyen@example.com", "addison.fisher@example.com", "jaxson.myers@example.com", "clara.watson@example.com",
    "jeremiah.brooks@example.com", "kylie.perry@example.com", "hudson.ramirez@example.com", "paisley.kim@example.com",
    "nathan.sullivan@example.com", "eliana.anderson@example.com", "jaden.gonzales@example.com",
    "valentina.wright@example.com", "colton.phillips@example.com", "paige.campbell@example.com",
    "richard.craig@example.com", "blake.craig@example.com", "laura.craig@example.com"
]


def main():
    bloom_filter = Bloom(1000, 3)


if __name__ == "__main__":
    main()
