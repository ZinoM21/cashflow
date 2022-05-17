def serialize_opportunities(opportunities):
    opportunities_list = []

    for opportunity in opportunities:
        opportunities_list.append({
            "id": opportunity.id,
            "type": opportunity.type,
            "category": opportunity.category, 
        })
    
    return opportunities_list