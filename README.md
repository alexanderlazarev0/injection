# Injection

### Features 

The dependecy injection library should support the following features:

- **Container**: manages a central registry for depencies & their lifetimes

```python
class MyContainer(Container): ...
```
- **Providers**: manage how the depenency is created (factory, singleton, instance)

```python
class FactoryProvider(Provider): ...
```

- **Injection**: ability to easily and automatically inject into any given function.

```python
@inject
def func(a: int = Injected(MyContainer.a)): ...
```

- **Configuration**: must work with ``pydantic`` out of the box

- **Overriding**: override dependency injection.

```python
with MyContainer.a.overide(FactoryProvider(a_override)):
    ...
```

- **Async support**: allow both sync and async dependency injection
    - *Optional*: allow using async resources in sync contexts using ``asyncer``.

- **Support generators**: auto wrap generators with contextmanagers and close them correctly after function calls.

