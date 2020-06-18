from solution import InventoryAllocator


def printResults(order, inventoryDistribution):
    print ("order: " + str(order))
    print("inventoryDistribution: " + str(inventoryDistribution))
    testAllocator = InventoryAllocator()
    shipment = testAllocator.allocate_order(order, inventoryDistribution)
    print("shipment: " + str(shipment))
    print("")

print("Test Case 1")
order = { "apple": 5 }
inventoryDistribution = [{ "name": "owd", "inventory": { "apple": 5 } }, { "name": "dm", "inventory": { "apple": 5 }}]
printResults(order, inventoryDistribution)

print("Test Case 2")
order = { "apple": 10 }
inventoryDistribution = [{ "name": "owd", "inventory": { "apple": 5 } }, { "name": "dm", "inventory": { "apple": 5 }}]
printResults(order, inventoryDistribution)

print("Test Case 3")
order = { "apple": 6 }
inventoryDistribution = [{ "name": "owd", "inventory": { "apple": 5 } }]
printResults(order, inventoryDistribution)

print("Test Case 4")
order = { "apple": 5, "banana": 5, "orange": 10 }
inventoryDistribution = [ { "name": "owd", "inventory": { "apple": 5, "orange": 5 } }, { "name": "dm", "inventory": { "banana": 5, "orange": 10 } } ]
printResults(order, inventoryDistribution)