---
records:
    - id: QRAQA095KW
      kind: monograph
      title: Spline Functions
      creators:
        - name: Klaus Böhmer
          role: editor
        - name: Günter Meinardus
          role: editor
        - name: Walter Schempp
          role: editor
      date: "1976"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 41-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1976"
          ids:
            doi: 10.1007/bfb0079739
            zbl: "0309.00029"
            zbl_id: "3483974"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1976"
              ids:
                isbn:
                    - "9783540075431"
                    - "9783540380733"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0079739
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3483974"
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
