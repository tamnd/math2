---
records:
    - id: NAV3D36V37
      kind: monograph
      title: Transformation Groups Poznań 1985
      creators:
        - name: Stefan Jackowski
          role: editor
        - name: Krzysztof Pawałowski
          role: editor
      date: "1986"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 57-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1986"
          ids:
            doi: 10.1007/bfb0072810
            zbl: "0594.00014"
            zbl_id: "3954837"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1986"
              ids:
                isbn:
                    - "9783540168249"
                    - "9783540470977"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0072810
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3954837"
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
