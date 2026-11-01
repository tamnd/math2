---
records:
    - id: YE2CTG3JRQ
      kind: problem-set
      title: Kvant 1984, no. 6
      creators:
        - name: Kvant editorial board
          role: editor
      date: "1984"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "1984"
          structure: YE2CTG3JRQ/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1984-6
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
    - id: YE2D6GVH00
      kind: edited-volume
      title: 'Convex and Complex: Perspectives on Positivity in Geometry'
      creators:
        - name: Robert Berman
          role: editor
        - name: Yanir Rubinstein
          role: editor
      date: "2025-01-20"
      msc:
        - code: 32-06
          from: zbmath_search
        - code: 32L05
          from: zbmath_search
        - code: 14C20
          from: zbmath_search
        - code: 32Q15
          from: zbmath_search
        - code: 32Q20
          from: zbmath_search
        - code: 52A40
          from: zbmath_search
        - code: 32U05
          from: zbmath_search
        - code: 32P05
          from: zbmath_search
        - code: 14G22
          from: zbmath_search
        - code: 32Q25
          from: zbmath_search
        - code: 53A15
          from: zbmath_search
        - code: 00B25
          from: zbmath_search
        - code: 00B30
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2025-01-20"
          ids:
            doi: 10.1090/conm/810
            zbl: "1555.32001"
            zbl_id: "7965527"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2025-01-20"
              ids:
                isbn:
                    - "9781470478612"
                    - "9781470473389"
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
          native_id: 10.1090/conm/810
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "7965527"
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
