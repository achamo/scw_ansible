# Scaleway Dynamic Inventory

It provides an executable script you can use with Ansible's /-i/ command line option.

# Configuration

You need a valid token in an environment variable /SCW_TOKEN/ (find how to get one https://developer.scaleway.com/#tokens-tokens-post).

It will use par1 as a default region, you can change this with /SCW_REGION/ environment variable.

# Examples

## Ams1

```
# SCW_REGION=ams1 ansible hareng -m shell -a "uptime"
hareng | SUCCESS | rc=0 >>
 23:18:08 up 26 min,  2 users,  load average: 0.08, 0.02, 0.01
```

## Default (par1)

```
# ansible fletan -m shell -a "uptime"
fletan | SUCCESS | rc=0 >>
 23:19:38 up 526 days,  2:38,  1 user,  load average: 2.70, 2.48, 2.44
```

