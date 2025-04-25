from django.utils.text import slugify

def generate_unique_slug(model_class, field_value, slug_field_name='slug'):
    """
    Generates a unique slug for a given model based on a field_value (e.g. title).

    Args:
        model_class: The model class to check for slug uniqueness.
        field_value: The text to slugify (e.g., post title).
        slug_field_name: The name of the slug field in the model (default: 'slug').

    Returns:
        A unique slug string.
    """
    slug_base = slugify(field_value)
    slug = slug_base

    counter = 1

    # Look up existing slugs in the model
    lookup = {slug_field_name: slug}
    while model_class.objects.filter(**lookup).exists():
        slug = f"{slug_base}-{counter}"
        lookup[slug_field_name] = slug
        counter += 1

    return slug
