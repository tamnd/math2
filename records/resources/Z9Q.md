---
records:
    - id: Z9QC8KZNKZ
      kind: monograph
      title: Group Theory
      creators:
        - name: Otto H. Kegel
          role: editor
        - name: Federico Menegazzo
          role: editor
        - name: Giovanni Zacher
          role: editor
      date: "1987"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 20-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1987"
          ids:
            doi: 10.1007/bfb0078683
            zbl: "0619.00010"
            zbl_id: "4004087"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1987"
              ids:
                isbn:
                    - "9783540183990"
                    - "9783540479482"
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
          native_id: 10.1007/bfb0078683
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "4004087"
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
