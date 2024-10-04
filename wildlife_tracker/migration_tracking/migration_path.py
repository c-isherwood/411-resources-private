from typing import Optional, List
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration import MigrationPath

class MigrationPath:

    pass

def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
    pass

def get_migration_path_by_id(path_id: int) -> MigrationPath:
    pass

def get_migration_paths() -> list[MigrationPath]:
    pass

def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:
    pass

def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
    pass

def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:
    pass

def remove_migration_path(path_id: int) -> None:
    pass

def update_migration_path_details(path_id: int, **kwargs) -> None:
    pass