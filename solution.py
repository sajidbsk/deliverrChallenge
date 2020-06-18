class InventoryAllocator:
    
    def allocate_order(self, order, inventoryDistribution):
        shipment = []

        for distributor in inventoryDistribution:
            result = {}
            for item, quantity in order.items():
                if distributor['inventory'].get(item):
                    result[item] = min(quantity, distributor['inventory'][item])
                    order[item] -= min(quantity, distributor['inventory'][item])
                    # Remove item from order if fulfilled
                    if order[item] == 0:
                        order.pop(item)
            if result:
                shipment.append({distributor['name'] : result})
            
            # Check if all item orders have been fulfilled by now
            if not order:
                break
        #If there are still unfulfilled orders
        if order:
            return []
        # [TODO: Remove shipment inventory from inventoryDistribution]
        return shipment
