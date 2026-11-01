---
records:
    - id: EJD0B1AK8A
      kind: monograph
      title: 'Metric Spaces: A Companion to Analysis'
      creators:
        - name: Robert Magnus
          role: author
          ids:
            orcid: 0000-0002-3147-2495
      date: "2022"
      msc:
        - code: 54-01
          from: zbmath_search
        - code: "54E35"
          from: zbmath_search
        - code: 26-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2022"
          ids:
            doi: 10.1007/978-3-030-94946-4
            zbl: "1484.54001"
            zbl_id: "7471586"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2022"
              ids:
                isbn:
                    - "9783030949457"
                    - "9783030949464"
              access:
                class: record
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-94946-4
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "7471586"
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
