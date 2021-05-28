Tester:
    resource_title: testers
    item_title: tester
    url: tester
    datasource:
        source: tester
    additional_lookup:
        url: string
        field: required_string
    cache_control: "max-age=10,must-revalidate"
    cache_expires: 10
    schema:
        required_string: {type: string, required: true, unique: true}
        string: {type: string}
        number: {type: number}
        media: {type: media}
