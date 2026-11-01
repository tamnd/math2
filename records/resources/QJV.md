---
records:
    - id: QJV0MQVCY8
      kind: monograph
      title: 'Mathematical Scattering Theory: General Theory'
      creators:
        - name: D. Yafaev
          role: author
      date: "1992-09-09"
      msc:
        - code: 47A40
          from: zbmath_search
        - code: 81U20
          from: zbmath_search
        - code: 47-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1992-09-09"
          ids:
            doi:
                - 10.1090/mmono/105
                - 10.1090/surv/158
            zbl: "0761.47001"
            zbl_id: "46774"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1992-09-09"
              ids:
                isbn:
                    - "9780821809518"
                    - "9780821897379"
                    - "9781470445164"
              access:
                class: record
            - key: m2
              kind: print
              publisher: American Mathematical Society
              date: "2010-03-10"
              ids:
                isbn:
                    - "9780821803318"
                    - "9781470413859"
              access:
                class: record
      relations:
        - kind: part_of
          to: BTDY0N3WC9
          source: cluster/1
        - kind: part_of
          to: M891DMMNP3
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/mmono/105
          level: work
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/surv/158
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "46774"
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
