""" Tests the scanner functions """
import activity_log_scanner.scanner as scanner
import os
import pytest

image_dir = os.path.join(os.path.dirname(__file__), 'images')

scan_data = [
    {
        'image': os.path.join(image_dir, 'Stephen Badger#90.png'),
        'output': {
            'EnemyPlayerDamage': 7457,
            'FriendlyPlayerDamage': 988,
            'EnemyStructureVehicleDamage': 29956,
            'FriendlyStructureVehicleDamage': 12569,
            'FriendlyConstruction': 23694,
            'FriendlyRepairing': 1916,
            'FriendlyHealing': 282,
            'FriendlyRevivals': 2,
            'VehiclesCapturedByEnemy': 0,
            'VehicleSelfDamage': 0,
            'MaterialsSubmitted': 95067,
            'MaterialsGathered': 47725,
            'SupplyValueDelivered': 86688
        }
    },
    {
        'image': os.path.join(image_dir, 'sneakysnipersnip#90.png'),
        'output': {
            'EnemyPlayerDamage': 75966,
            'FriendlyPlayerDamage': 4076,
            'EnemyStructureVehicleDamage': 377643,
            'FriendlyStructureVehicleDamage': 15567,
            'FriendlyConstruction': 24853,
            'FriendlyRepairing': 7119,
            'FriendlyHealing': 6798,
            'FriendlyRevivals': 29,
            'VehiclesCapturedByEnemy': 1,
            'VehicleSelfDamage': 5327,
            'MaterialsSubmitted': 388501,
            'MaterialsGathered': 264312,
            'SupplyValueDelivered': 241654
        }
    },
    {
        'image': os.path.join(image_dir, 'sneakysnipersnip#90 - Screen.jpg'),
        'output': {
            'EnemyPlayerDamage': 75966,
            'FriendlyPlayerDamage': 4076,
            'EnemyStructureVehicleDamage': 377643,
            'FriendlyStructureVehicleDamage': 15567,
            'FriendlyConstruction': 24853,
            'FriendlyRepairing': 7119,
            'FriendlyHealing': 6798,
            'FriendlyRevivals': 29,
            'VehiclesCapturedByEnemy': 1,
            'VehicleSelfDamage': 5327,
            'MaterialsSubmitted': 388501,
            'MaterialsGathered': 264312,
            'SupplyValueDelivered': 241654
        }
    }
]

@pytest.mark.parametrize('data', scan_data)
def test_scan(data):
    assert scanner.scan(data['image']) == data['output']