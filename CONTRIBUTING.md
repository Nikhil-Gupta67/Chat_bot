# Contributing Guide

Thank you for your interest in contributing to the Django Chatbot Application!

## Getting Started

### 1. Fork and Clone

```bash
git clone https://github.com/yourusername/chatbot.git
cd chatbot
```

### 2. Set Up Development Environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

## Development Guidelines

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and under 50 lines when possible

### Example:

```python
def get_bot_response(message: str) -> tuple[str, float]:
    """
    Generate a bot response for the given user message.

    Args:
        message: The user's input message

    Returns:
        A tuple containing the response text and confidence score
    """
    # Implementation here
    return response, confidence
```

### Testing

- Write tests for new features
- Run tests before submitting PR: `python manage.py test blog`
- Aim for at least 80% code coverage

### Example Test:

```python
class NewFeatureTestCase(TestCase):
    def test_feature_behavior(self):
        """Test the new feature works correctly"""
        result = new_feature()
        self.assertEqual(result, expected_value)
```

## Areas for Contribution

### 1. New Response Patterns

Add new conversation patterns to make the bot smarter:

```python
# In views.py, add_to get_bot_response():
if 'pattern' in message:
    return "Response to pattern", confidence_score
```

### 2. UI Improvements

- Enhance the chat interface styling
- Add new features to the frontend
- Improve mobile responsiveness

### 3. API Enhancements

- Add new endpoints
- Improve error handling
- Add rate limiting

### 4. Documentation

- Improve README and guides
- Add code comments
- Create tutorials

### 5. Performance

- Optimize database queries
- Improve response generation
- Reduce memory usage

## Submitting Changes

### 1. Commit Messages

Use clear, descriptive commit messages:

```bash
git commit -m "Add support for weather queries in bot responses"
```

Good commit messages:

- Start with a verb (Add, Fix, Improve, Refactor)
- Be specific about what changed
- Keep under 50 characters for subject line

### 2. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a PR on GitHub with:

- Clear title describing the change
- Description of what was changed and why
- Reference to related issues
- Screenshots for UI changes

### 3. PR Template

```markdown
## Description

Brief description of changes

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Enhancement
- [ ] Documentation

## Testing

- [ ] Unit tests added
- [ ] Tests pass locally
- [ ] No new warnings

## Screenshots (if applicable)

Add screenshots for UI changes

## Checklist

- [ ] Code follows style guidelines
- [ ] Docstrings added
- [ ] No debug code left
- [ ] Works on Windows/Mac/Linux
```

## Running Tests

### Run all tests

```bash
python manage.py test blog
```

### Run specific test class

```bash
python manage.py test blog.tests.BotResponseTestCase
```

### Run with coverage

```bash
pip install coverage
coverage run --source='blog' manage.py test blog
coverage report
coverage html  # Creates htmlcov/index.html
```

## Database Migrations

If you modify models:

```bash
python manage.py makemigrations blog
python manage.py migrate
```

Always commit migration files to version control.

## Adding New Features

### Step 1: Create a feature branch

```bash
git checkout -b feature/my-feature
```

### Step 2: Modify files

- Update models if needed
- Create migrations
- Update views/serializers
- Add tests
- Update documentation

### Step 3: Test thoroughly

```bash
python manage.py test blog -v 2
```

### Step 4: Check code quality

```bash
# Optional: Install and run linters
pip install flake8 black isort
flake8 blog/
black blog/
isort blog/
```

## Reporting Issues

When reporting bugs, include:

- Python and Django versions
- Steps to reproduce
- Expected vs actual behavior
- Error messages and tracebacks
- Screenshots if applicable

### Issue Template

```markdown
## Bug Description

Brief description of the bug

## Steps to Reproduce

1. Step one
2. Step two
3. Step three

## Expected Behavior

What should happen

## Actual Behavior

What actually happens

## Environment

- Python: 3.10
- Django: 6.0
- OS: Windows/Mac/Linux
```

## Code Review Process

Your PR will be reviewed by maintainers:

- Code quality and style check
- Test coverage verification
- Security review
- Documentation review
- Performance impact assessment

Please be open to feedback and willing to make requested changes.

## Coding Standards

### Python Code

```python
# Good
def calculate_confidence(responses):
    """Calculate average confidence score."""
    if not responses:
        return 0.0
    return sum(r.score for r in responses) / len(responses)

# Avoid
def calc_conf(r):  # Unclear naming
    total = 0
    for x in r:  # Poor variable names
        total += x.score
    return total / len(r)
```

### Model Conventions

```python
class MyModel(models.Model):
    """Model for storing my data."""

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [models.Index(fields=['created_at'])]

    def __str__(self):
        return self.name
```

### Template Best Practices

```html
<!-- Good: Clear variable names and structure -->
<div class="message-container">
  {% for message in messages %}
  <div class="message">{{ message.text }}</div>
  {% endfor %}
</div>

<!-- Avoid: Unclear structure -->
<div>
  {% for m in x %}
  <div>{{ m }}</div>
  {% endfor %}
</div>
```

## Performance Guidelines

- Use `select_related()` and `prefetch_related()` for queries
- Avoid N+1 queries
- Use database indexes for frequently queried fields
- Cache expensive operations
- Minimize database hits

## Security Considerations

- Sanitize user input
- Use Django's built-in security features
- Never commit secrets or passwords
- Validate all API inputs
- Use CSRF protection
- Implement rate limiting

## Documentation

When adding features, update:

- Docstrings in code
- README.md
- CHANGELOG.md
- Create examples if needed

## Licensing

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

- Open an issue for questions
- Check existing documentation
- Review similar code in the project
- Ask in PRs/issues

Thank you for contributing! 🎉
