---
records:
    - id: 8YK7PSWA0V
      kind: monograph
      title: Répartition Modulo 1
      creators:
        - name: Gérard Rauzy
          role: editor
      date: "1975"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 11-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: fr
          date: "1975"
          ids:
            doi: 10.1007/bfb0074253
            zbl: "0299.00015"
            zbl_id: "3468706"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1975"
              ids:
                isbn:
                    - "9783540073888"
                    - "9783540375791"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0074253
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3468706"
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
