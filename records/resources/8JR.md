---
records:
    - id: 8JR99DR1R2
      kind: edited-volume
      title: 'Inverse Problems: Theory and Applications'
      creators:
        - name: Giovanni Alessandrini
          role: editor
        - name: Gunther Uhlmann
          role: editor
      date: "2003"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 35-06
          from: zbmath_search
        - code: 35R30
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2003"
          ids:
            doi: 10.1090/conm/333
            zbl: "1027.00018"
            zbl_id: "2017022"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2003"
              ids:
                isbn:
                    - "9780821833674"
                    - "9780821856680"
                    - "9780821879238"
              access:
                class: record
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/333
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "2017022"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
